from api.base_api import BaseApi

class PostApi(BaseApi):

    def get_posts(self):
        return self.get("/posts")
    
    def create_post(self, payload):
        return self.post("/posts", payload)

    def update_post(self, post_id, payload):
        return self.put(f"/posts/{post_id}", payload)

    def delete_post(self, post_id):
        return self.delete(f"/posts/{post_id}")