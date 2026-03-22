from flask import Blueprint, request, jsonify
from .models import Post
from .database import db

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return {"message": "Blog API is running 🚀"}

# Create Post
@main.route("/posts", methods=["POST"])
def create_post():
    data = request.json

    if not data or not data.get("title") or not data.get("content"):
        return jsonify({"error": "Title and content required"}), 400

    post = Post(
        title=data["title"],
        content=data["content"]
    )

    db.session.add(post)
    db.session.commit()

    return jsonify(post.to_dict()), 201


# Get All Posts
@main.route("/list", methods=["GET"])
def get_posts():
    posts = Post.query.order_by(Post.id.desc()).all()
    return jsonify([p.to_dict() for p in posts])


# Get Single Post
@main.route("/list/<int:id>", methods=["GET"])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.to_dict())


# Update Post
@main.route("/update/<int:id>", methods=["PUT"])
def update_post(id):
    post = Post.query.get_or_404(id)
    data = request.json

    if "title" in data:
        post.title = data["title"]
    if "content" in data:
        post.content = data["content"]

    db.session.commit()

    return jsonify(post.to_dict())


# Delete Post
@main.route("/delete/<int:id>", methods=["DELETE"])
def delete_post(id):
    post = Post.query.get_or_404(id)

    db.session.delete(post)
    db.session.commit()

    return jsonify({"message": "Deleted"})