class Comment:
    def __init__ (self,content,comment_id,comment_date,user_id):
        self.content=content
        self.comment_id=comment_id
        self.comment_date=comment_date
        self.user_id=user_id
        
    def get_date(self):
        return self.comment_date
        
    def get_content(self):
        return self.content
        
    def set_content(self,content):
        self.content=content
            