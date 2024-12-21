#!/usr/bin/env python3
import rclpy
import time
import threading
from rclpy.node import Node
from rclpy.action import ActionServer, GoalResponse, CancelResponse
from rclpy.action.server import ServerGoalHandle
from my_robot_interfaces.action import MoveToTarget
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup


class MoveToTargetServerNode(Node):
    def __init__(self):
        super().__init__("move_to_target_server")
        self.current_position_ = 50
        self.goal_handle_: ServerGoalHandle = None
        self.goal_lock_ = threading.Lock()
        self.move_to_target_server_ = ActionServer(
                                                        self, 
                                                        MoveToTarget, 
                                                        "move_to_target",
                                                        goal_callback=self.goal_callback,
                                                        handle_accepted_callback=self.handle_accepted_callback,
                                                        cancel_callback=self.cancle_callback,
                                                        execute_callback=self.execute_callback,
                                                        callback_group=ReentrantCallbackGroup())
        self.get_logger().info("Action Server has been started")
        self.get_logger().info("Robot Act_position:" + str(self.current_position_))

    def goal_callback(self,goal_request: MoveToTarget.Goal):
        self.get_logger().info("Recieved a goal")

        # validate the goal request
        if goal_request.position < 0 or goal_request.position > 100 :
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
    
    def handle_accepted_callback(self, goal_handle: ServerGoalHandle):
        goal_handle.execute()

    def execute_callback(self, goal_handle: ServerGoalHandle):
        with self.goal_lock_ :
            self.goal_handle_ = goal_handle


        # Get request from Goal
        target_position = goal_handle.request.position
        target_velocity = goal_handle.request.velocity

        # Execute the action
        self.get_logger().info("Executing the Goal")
        feedback = MoveToTarget.Feedback()
        result = MoveToTarget.Result()

        while rclpy.ok():
            diff = target_position - self.current_position_ 

            if diff == 0:
                result.position = self.current_position_
                result.message = "Success"
                goal_handle.succeed()
                return result

            elif diff > 0:
                if diff >= target_velocity:
                    self.current_position_ += target_velocity
                else:
                    self.current_position_ += diff
            else:
                if abs(diff) >= target_velocity:
                    self.current_position_ -= target_velocity
                else:
                    self.current_position_ -= abs(diff)

            self.get_logger().info("Robot Act_position:" + str(self.current_position_))
            feedback.current_position = self.current_position_
            goal_handle.publish_feedback(feedback)
            time.sleep(1)
            

        # while self.current_position_ != target_position:
        #     if not goal_handle.is_active:
        #         result.position = self.current_position_
        #         result.message = "Abort By New Goal"
        #         return result
            
        #     if goal_handle.is_cancel_requested:
        #         self.get_logger().info("Canceling the Goal")
        #         goal_handle.canceled()
        #         result.position = self.current_position_
        #         result.message = "Abort By New Goal"
        #         return result

        #     if abs(self.current_position_ - target_position) > target_velocity:
        #         if self.current_position_ < target_position :
        #             self.current_position_ = self.current_position_ + target_velocity
        #         else:
        #             self.current_position_ = self.current_position_ - target_velocity
        #     else:
        #         self.current_position_ = target_position

        #     self.get_logger().info(str(self.current_position_))
        #     feedback.current_position = self.current_position_
        #     goal_handle.publish_feedback(feedback)
        #     time.sleep(1)

        # #Once done, set goal final state
        # goal_handle.succeed()

        # #and send the result  
        # result.position = self.current_position_
        # result.message = "Success"
        # return result

def main(args=None):
    rclpy.init(args=args)
    node = MoveToTargetServerNode()
    rclpy.spin(node, MultiThreadedExecutor())
    rclpy.shutdown()


if __name__ == "__main__":
    main()