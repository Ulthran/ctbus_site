terraform {
  backend "s3" {
    bucket       = "ctbus-tfstates"
    key          = "ctbus_site/games.tfstate"
    region       = "us-east-1"
    use_lockfile = true
    encrypt      = true
  }
}
