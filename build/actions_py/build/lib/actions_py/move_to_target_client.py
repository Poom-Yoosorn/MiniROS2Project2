#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.action.client import ClientGoalHandle , GoalStatus
from my_robot_interfaces.action import MoveToTarget


class MoveToTargetClientNode(Node):
    def __init__(self):
        super().__init__("move_to_target_client")
        self.move_to_target_client_ = ActionClient(self,
                                                MoveToTarget,
                                                "move_to_target")
        
    def send_goal(self, target_position, target_velocity):
        #Wait for the server
        self.move_to_target_client_.wait_for_server()

        #Create a goal
        goal = MoveToTarget.Goal()
        goal.position = target_position
        goal.velocity = target_velocity

        #Send the Goal
        self.get_logger(). \
            info("Sending goal with target position" + str(target_position) + "and target velocity" + str(target_velocity))
        self.move_to_target_client_. \
            send_goal_async(goal, feedback_callback=self.goal_feedback_callback). \
            add_done_callback(self.goal_response_callback)
    
    def cancel_goal(self):
        self.get_logger().info("Send a cancel request")
        self.goal_handle_.cancel_goal_async()
        self.timer_.cancel()

        
    def goal_response_callback(self, future):
        self.goal_handle_ : ClientGoalHandle = future.result()
        if self.goal_handle_.accepted:
            self.get_logger().info("Goal got accepted")
            self.goal_handle_.get_result_async().add_done_callback(self.goal_result_callback)
        else:
            self.get_logger().warn("Goal got rejected")

    def goal_result_callback(self, future):
        status = future.result().status
        result = future.result().result
        if status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info("Successed")
        elif status == GoalStatus.STATUS_ABORTED:
            self.get_logger().error("Aborted")
        elif status == GoalStatus.STATUS_CANCELED:
            self.get_logger().warn("Canceled")

        self.get_logger().info("Result Position: " + str(result.position))
        self.get_logger().info("Result Message: " + str(result.message))


    def goal_feedback_callback(self, feedback_msg):
        current_position = feedback_msg.feedback.current_position
        self.get_logger().info("Got Feedback Position: " + str(current_position))

    

def main(args=None):
    rclpy.init(args=args)
    node = MoveToTargetClientNode()
    node.send_goal(75 ,3)
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()