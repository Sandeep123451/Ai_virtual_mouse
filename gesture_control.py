import pyautogui


class GestureControl:
    def __init__(self, screen_width, screen_height, click_threshold=0.05):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.click_threshold = click_threshold  # Threshold for detecting a click gesture
        self.clicking = False  # To prevent multiple clicks in one gesture

    def move_mouse(self, index_finger_tip):
        # Convert hand landmark to screen coordinates
        x = int(index_finger_tip.x * self.screen_width)
        y = int(index_finger_tip.y * self.screen_height)
        # Move the mouse
        pyautogui.moveTo(x, y)

    def click(self, thumb_tip, index_finger_tip):
        # Calculate the distance between thumb and index finger
        distance = ((thumb_tip.x - index_finger_tip.x) ** 2 + (thumb_tip.y - index_finger_tip.y) ** 2) ** 0.5

        # Detect click gesture
        if distance < self.click_threshold:
            if not self.clicking:
                pyautogui.click()  # Trigger mouse click
                self.clicking = True
        else:
            self.clicking = False  # Reset the clicking state for the next gesture
