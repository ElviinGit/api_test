from api.base_api import BaseApi

class UsersApi(BaseApi):
    """API endpoints for Users"""

    def get_users(self):
        """Get all users"""
        return self.get("/users")
    
    def get_user(self, user_id):
        """Get specific user by ID"""
        return self.get(f"/users/{user_id}")
    
    def create_user(self, payload):
        """Create a new user"""
        return self.post("/users", payload)

    def update_user(self, user_id, payload):
        """Update a specific user"""
        return self.put(f"/users/{user_id}", payload)

    def delete_user(self, user_id):
        """Delete a specific user"""
        return self.delete(f"/users/{user_id}")


class CommentsApi(BaseApi):
    """API endpoints for Comments"""

    def get_comments(self):
        """Get all comments"""
        return self.get("/comments")
    
    def get_comment(self, comment_id):
        """Get specific comment by ID"""
        return self.get(f"/comments/{comment_id}")
    
    def get_post_comments(self, post_id):
        """Get comments for a specific post"""
        return self.get(f"/comments?postId={post_id}")
    
    def create_comment(self, payload):
        """Create a new comment"""
        return self.post("/comments", payload)

    def update_comment(self, comment_id, payload):
        """Update a specific comment"""
        return self.put(f"/comments/{comment_id}", payload)

    def delete_comment(self, comment_id):
        """Delete a specific comment"""
        return self.delete(f"/comments/{comment_id}")
