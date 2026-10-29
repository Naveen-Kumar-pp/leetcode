
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Create a dummy node to start the result linked list
        dummy = ListNode(0)
        current = dummy

        # Carry stores the extra value from addition
        carry = 0

        # Continue while either list has nodes or carry remains
        while l1 or l2 or carry:

            # Get the current digits, or 0 if a list has ended
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Add both digits and the carry
            total = x + y + carry

            # Calculate the result digit and the next carry
            digit = total % 10
            carry = total // 10

            # Create a new node for the result digit
            current.next = ListNode(digit)

            # Move to the next result node
            current = current.next

            # Move to the next input nodes if they exist
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        # Return the head of the result linked list
        return dummy.next

