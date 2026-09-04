output "nginx_container_name" {
  description = "Name of the nginx container"
  value       = docker_container.nginx.name
}
