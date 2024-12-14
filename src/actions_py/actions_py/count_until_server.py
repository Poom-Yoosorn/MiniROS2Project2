#!/usr/bin/env python3
import rclpy
import time
import threading
from rclpy.node import Node
from rclpy.action import ActionServer, GoalResponse, CancelResponse
from rclpy.action.server import ServerGoalHandle
from my_robot_interfaces.action import CountUntil
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup

class CountUntilServerNode(Node):
    def __init__(self):
        super().__init__("count_until_server")
        self.goal_handle_: ServerGoalHandle = None
        self.goal_lock_ = threading.Lock()
        self.count_until_server_ = ActionServer(
                                                  self, 
                                                  CountUntil, 
                                                  "count_until",
                                                  goal_callback=self.goal_callback,
                                                  cancel_callback=self.cancle_callback,
                                                  execute_callback=self.execute_callback,
                                                  callback_group=ReentrantCallbackGroup())
        self.get_logger().info("Action Server has been started")

    def goal_callback(self,goal_request: CountUntil.Goal):
        self.get_logger().info("Recieved a goal")

        # #Policy: refuse new goal if current goal still active
        # with self.goal_lock_ :
        #     if self.goal_handle_ is not None and self.goal_handle_.is_active:
        #         self.get_logger().info("A goal is already active, rejecting new goal")
        #         return GoalResponse.REJECT

        # validate the goal request
        if goal_request.target_number <= 0:
            self.get_logger().info("Rejecting the goal")
            return GoalResponse.REJECT
        
        #Policy: preempt existing goal when receiving new goal
        with self.goal_lock_ :
            if self.goal_handle_ is not None and self.goal_handle_.is_active:
                self.get_logger().info("Abort current goal and accept new goal")
                self.goal_handle_.abort()

        self.get_logger().info("Accepting the goal")
        return GoalResponse.ACCEPT
    

    def cancle_callback(self, goal_handle: ServerGoalHandle):
        self.get_logger().info("Recieve a cancel request")
        return CancelResponse.ACCEPT # or REJECT



    def execute_callback(self, goal_handle: ServerGoalHandle):
        with self.goal_lock_ :
            self.goal_handle_ = goal_handle

        # Get request from Goal
        target_number = goal_handle.request.target_number
        period = goal_handle.request.period

        # Execute the action
        self.get_logger().info("Executing the Goal")
        feedback = CountUntil.Feedback()
        result = CountUntil.Result()
        counter = 0
        for i in range(target_number):
            if not goal_handle.is_active:
                result.reached_number = counter
                return result
            
            if goal_handle.is_cancel_requested:
                self.get_logger().info("Canceling the Goal")
                goal_handle.canceled()
                result.reached_number = counter
                return result
            counter += 1
            self.get_logger().info(str(counter))
            feedback.current_number = counter
            goal_handle.publish_feedback(feedback)
            time.sleep(period)

        #Once done, set goal final state
        goal_handle.succeed()

        #and send the result  
        result.reached_number = counter
        return result

def main(args=None):
    rclpy.init(args=args)
    node = CountUntilServerNode()
    rclpy.spin(node, MultiThreadedExecutor())
    rclpy.shutdown()


if __name__ == "__main__":
    main()