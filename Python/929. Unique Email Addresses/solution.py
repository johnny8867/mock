class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()

        for email in emails:
            local, domain = email.split('@')

            local = local.split('+')[0]
            local = ''.join(local.split('.'))
            to_add = local +'@' +domain
            result.add(to_add)

        return len(result)
        #O(N), O(N)