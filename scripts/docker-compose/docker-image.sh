function push_image () {
    docker push 
}

function build_image() {
    docker build -f /path/to/a/Dockerfile -t image_repo/image_tag
}