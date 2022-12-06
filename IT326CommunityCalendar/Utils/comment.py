class Comment:

    #constructor
    def __init__(self, content, comment_id, comment_date, user_id):
        self.content = content 
        self.comment_id = comment_id
        self.comment_date = comment_date
        self.user_id = user_id

    
    def get_date(self):
        '''Getter for the date instance variable'''
        return self.comment_date

    def get_content(self):
        '''Getter for the content instance variable'''
        return self.content

    def set_content(self, content):
        '''Setter for the content instance variable'''
        self.content = content

    def get_comment_id(self, comment_id):
        '''Getter for the comment Id instance variable'''
        return self.comment_id

    def get_user_id(self, user_id):
        '''Getter for the user Id instance variable'''
        return self.user_id
