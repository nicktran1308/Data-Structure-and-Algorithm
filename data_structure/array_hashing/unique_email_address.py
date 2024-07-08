"""
929. Unique Email Addresses

Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

 

Example 1:

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
Example 2:

Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3
 

Constraints:

1 <= emails.length <= 100
1 <= emails[i].length <= 100
emails[i] consist of lowercase English letters, '+', '.' and '@'.
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
Domain names end with the ".com" suffix.
"""

from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()  # Use a set to store unique normalized emails

        for email in emails:
            local, domain = email.split(
                "@"
            )  # Split the email into local and domain parts

            # Remove all characters after the first plus in the local part
            if "+" in local:
                local = local[: local.index("+")]

            # Remove all periods from the local part
            local = local.replace(".", "")

            # Create the normalized email and add it to the set
            normalized_email = f"{local}@{domain}"
            unique_emails.add(normalized_email)

        # The size of the set is the number of unique emails
        return len(unique_emails)


"""
Time Complexity: O(n*l), n: number of emails, l: average length of an email

Space Complexity: O(n*l), in worst case, all emails could be unique after normalization

Processing Each Email:
    First Email: "test.email+alex@leetcode.com"

        Split into local = "test.email+alex" and domain = "leetcode.com".
        Trim local after the plus: "test.email" (ignore "alex").
        Remove all periods: "testemail".
        Normalize and combine: "testemail@leetcode.com".
        Add to the set: unique_emails = {"testemail@leetcode.com"}.
        
    Second Email: "test.e.mail+bob.cathy@leetcode.com"

    Split into local = "test.e.mail+bob.cathy" and domain = "leetcode.com".
    Trim local after the plus: "test.e.mail" (ignore "bob.cathy").
    Remove all periods: "testemail".
    Normalize and combine: "testemail@leetcode.com".
    Add to the set: unique_emails = {"testemail@leetcode.com"} (no change, as it's already present).

"""
