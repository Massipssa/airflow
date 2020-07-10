
IMAGE=$USERNAME/$IMAGE_NAME:$VERSION

case $1 in
  push)
    push_image
  ;;
  build)
    build_image
esac

function push_image {
  echo "Start building image"
  echo
  docker login -u "$USERNAME" -p "$PASSWORD"
  docker build -t "$IMAGE" .
  docker push "$IMAGE"
  echo "Image $IMAGE pushed to Docker Hub"
}

function build_image() {
    docker build -t IMAGE
}