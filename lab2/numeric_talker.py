import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int8


class Talker(Node):
    def __init__(self):
        super().__init__('talker')

        # String publisher (existing)
        self.string_publisher = self.create_publisher(String, 'chatter', 10)

        # Int8 publisher (new)
        self.numeric_publisher = self.create_publisher(
            Int8, 'numeric_chatter', 10)

        timer_in_seconds = 0.5
        self.timer = self.create_timer(timer_in_seconds, self.talker_callback)

        self.counter = 0

    def talker_callback(self):
        # Publish String message
        string_msg = String()
        string_msg.data = f'Hello World, {self.counter}'
        self.string_publisher.publish(string_msg)
        self.get_logger().info(f'Publishing: {string_msg.data}')

        # Publish Int8 message
        numeric_msg = Int8()
        numeric_msg.data = self.counter
        self.numeric_publisher.publish(numeric_msg)
        self.get_logger().info(f'Publishing: {numeric_msg.data}')

        # Increment and wrap counter at 127
        self.counter += 1
        if self.counter > 127:
            self.counter = 0


def main(args=None):
    rclpy.init(args=args)
    talker = Talker()
    rclpy.spin(talker)


if __name__ == '__main__':
    main()
