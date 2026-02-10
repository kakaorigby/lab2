import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int8


class Listener(Node):
    def __init__(self):
        super().__init__('listener')

        # Subscription to String chatter
        self.string_subscription = self.create_subscription(
            String,
            'chatter',
            self.string_listener_callback,
            10
        )

        # Subscription to numeric chatter
        self.numeric_subscription = self.create_subscription(
            Int8,
            'numeric_chatter',
            self.numeric_listener_callback,
            10
        )

    def string_listener_callback(self, msg):
        self.get_logger().info(f'I heard (string): {msg.data!r}')

    def numeric_listener_callback(self, msg):
        self.get_logger().info(f'I heard (numeric): {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    listener = Listener()
    rclpy.spin(listener)


if __name__ == '__main__':
    main()
