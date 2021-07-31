class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        validEmails = {}
        emailList = []
        m = []
        
        for index,email in enumerate(emails):
            email_type_list = []
            for index1, char in enumerate(email):
                email_type_list.append(char)
            emailList.append(email_type_list)
        
        for index, email_list in enumerate(emailList):
            ignore = False
            toAppendEmail = ""
            notSeenAt = True
            notSeenPlus = True
            
            for index1, char in enumerate(email_list):
                if char =="@":
                    notSeenAt = False
                if char == "+":
                    notSeenPlus = False
                if char != "." and notSeenAt == True and notSeenPlus == True:
                    toAppendEmail += char
                if notSeenAt == False:
                    toAppendEmail += char
            print(toAppendEmail)
            
            if toAppendEmail not in validEmails:
                validEmails[toAppendEmail] = 1
            else:
                validEmails[toAppendEmail] += 1
        
        print(validEmails)
        return len(validEmails)
                
                    

                    


        
            
        
