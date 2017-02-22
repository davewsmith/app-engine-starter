# App Engine Python Starter VM

Here's a starting point for Google App Engine projects, in Virtual Machine form.

This scratches an itch I have, and may require some fiddling to scratch yours. Fiddle away.

## Requirements

Building the VM requires VirtualBox and Vagrant. If you're running Ubuntu

    sudo apt-get install virtualbox

gets you the former, and following the instructions on `http://vagrant.io` gets you the latter

## Building a VM

Pull this down from github, then

    vagrant up

On my Linux laptop, with an SSD and over a mediocre network connection, it takes about 7 minutes to build a VM.

Then `vagrant ssh` into the VM to develop, test, and deploy.

## Developing

`make dev` will kick off `dev_appserver`. In the host OS, the application will be available on `http://localhost:8080/`, and the admin server will be available on `http://localhost:8000/`.

Reload-on-change isn't working inside the VirtualBox guest OS. There's a trail of bug reports on the internets. If you find a solution that's amenable to pull requests, please send me one.

## Testing

`make test` runs any tests.

## Deploying

`make deploy` deploys the application to App Engine.

This requires the environment variable `APP` to be set to the name of the application (as registered with App Engine), and make require a `gcloud init` to log in and cache credentials.

## License

No license. This is unwarrantied, use-at-your-own-riskware. It's mostly pieced together from App Engine documentation and public sources, plus a tiny bit of my own code that you're welcome to.

