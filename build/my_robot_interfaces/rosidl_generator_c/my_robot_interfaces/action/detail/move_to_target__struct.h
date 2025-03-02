// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_robot_interfaces:action/MoveToTarget.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__ACTION__DETAIL__MOVE_TO_TARGET__STRUCT_H_
#define MY_ROBOT_INTERFACES__ACTION__DETAIL__MOVE_TO_TARGET__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in action/MoveToTarget in the package my_robot_interfaces.
typedef struct my_robot_interfaces__action__MoveToTarget_Goal
{
  /// m
  int64_t position;
  /// m/s
  int64_t velocity;
} my_robot_interfaces__action__MoveToTarget_Goal;

// Struct for a sequence of my_robot_interfaces__action__MoveToTarget_Goal.
typedef struct my_robot_interfaces__action__MoveToTarget_Goal__Sequence
{
  my_robot_interfaces__action__MoveToTarget_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__action__MoveToTarget_Goal__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
#include "rosidl_runtime_c/string.h"

/// Struct defined in action/MoveToTarget in the package my_robot_interfaces.
typedef struct my_robot_interfaces__action__MoveToTarget_Result
{
  /// m
  int64_t position;
  rosidl_runtime_c__String message;
} my_robot_interfaces__action__MoveToTarget_Result;

// Struct for a sequence of my_robot_interfaces__action__MoveToTarget_Result.
typedef struct my_robot_interfaces__action__MoveToTarget_Result__Sequence
{
  my_robot_interfaces__action__MoveToTarget_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__action__MoveToTarget_Result__Sequence;


// Constants defined in the message

/// Struct defined in action/MoveToTarget in the package my_robot_interfaces.
typedef struct my_robot_interfaces__action__MoveToTarget_Feedback
{
  int64_t current_position;
} my_robot_interfaces__action__MoveToTarget_Feedback;

// Struct for a sequence of my_robot_interfaces__action__MoveToTarget_Feedback.
typedef struct my_robot_interfaces__action__MoveToTarget_Feedback__Sequence
{
  my_robot_interfaces__action__MoveToTarget_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__action__MoveToTarget_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "my_robot_interfaces/action/detail/move_to_target__struct.h"

/// Struct defined in action/MoveToTarget in the package my_robot_interfaces.
typedef struct my_robot_interfaces__action__MoveToTarget_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  my_robot_interfaces__action__MoveToTarget_Goal goal;
} my_robot_interfaces__action__MoveToTarget_SendGoal_Request;

// Struct for a sequence of my_robot_interfaces__action__MoveToTarget_SendGoal_Request.
typedef struct my_robot_interfaces__action__MoveToTarget_SendGoal_Request__Sequence
{
  my_robot_interfaces__action__MoveToTarget_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__action__MoveToTarget_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/MoveToTarget in the package my_robot_interfaces.
typedef struct my_robot_interfaces__action__MoveToTarget_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} my_robot_interfaces__action__MoveToTarget_SendGoal_Response;

// Struct for a sequence of my_robot_interfaces__action__MoveToTarget_SendGoal_Response.
typedef struct my_robot_interfaces__action__MoveToTarget_SendGoal_Response__Sequence
{
  my_robot_interfaces__action__MoveToTarget_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__action__MoveToTarget_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/MoveToTarget in the package my_robot_interfaces.
typedef struct my_robot_interfaces__action__MoveToTarget_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} my_robot_interfaces__action__MoveToTarget_GetResult_Request;

// Struct for a sequence of my_robot_interfaces__action__MoveToTarget_GetResult_Request.
typedef struct my_robot_interfaces__action__MoveToTarget_GetResult_Request__Sequence
{
  my_robot_interfaces__action__MoveToTarget_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__action__MoveToTarget_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "my_robot_interfaces/action/detail/move_to_target__struct.h"

/// Struct defined in action/MoveToTarget in the package my_robot_interfaces.
typedef struct my_robot_interfaces__action__MoveToTarget_GetResult_Response
{
  int8_t status;
  my_robot_interfaces__action__MoveToTarget_Result result;
} my_robot_interfaces__action__MoveToTarget_GetResult_Response;

// Struct for a sequence of my_robot_interfaces__action__MoveToTarget_GetResult_Response.
typedef struct my_robot_interfaces__action__MoveToTarget_GetResult_Response__Sequence
{
  my_robot_interfaces__action__MoveToTarget_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__action__MoveToTarget_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "my_robot_interfaces/action/detail/move_to_target__struct.h"

/// Struct defined in action/MoveToTarget in the package my_robot_interfaces.
typedef struct my_robot_interfaces__action__MoveToTarget_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  my_robot_interfaces__action__MoveToTarget_Feedback feedback;
} my_robot_interfaces__action__MoveToTarget_FeedbackMessage;

// Struct for a sequence of my_robot_interfaces__action__MoveToTarget_FeedbackMessage.
typedef struct my_robot_interfaces__action__MoveToTarget_FeedbackMessage__Sequence
{
  my_robot_interfaces__action__MoveToTarget_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__action__MoveToTarget_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_ROBOT_INTERFACES__ACTION__DETAIL__MOVE_TO_TARGET__STRUCT_H_
