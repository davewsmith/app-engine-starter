# App Engine Python Starter VM

This sets up a VirtualBox VM for developing a Google App Engine project, including the SDK, and a trivial app with initial tests.

Having a starting point within reach scratches an itch I have. It may require some fiddling to scratch yours. Fiddle away. I recommend working through at least one app engine app (e.g., the example app) before trying this.

## Requirements

Building the VM requires VirtualBox and Vagrant. If you're running Ubuntu,

    sudo apt-get install virtualbox

gets you the former, and following the instructions on `http://vagrant.io` gets you the latter. If you're on some other platform, follow whatever instructions you need to to get VirtualBox and Vagrant set up.

## Building the VM

Pull this project down from github, then

    vagrant up

On my Linux laptop, with an SSD and over a mediocre network connection, it takes about 7 minutes to build the VM.

## Developing

`vagrant ssh` into the VM and `cd /vagrant` to develop, test, and deploy. `/vagrant` in the guest is shared with the project directory on host, so you can edit app files outside of the VM.

`make dev` will kick off `dev_appserver`. In the host OS, the application will be available on `http://localhost:8080/`, and the admin server will be available on `http://localhost:8000/`.

Reload-on-change isn't working inside the VirtualBox guest OS, so you'll need to restart `dev_appserver` to see code changes. (There's a trail of bug reports about this on the internets. If you find a solution that's amenable to pull requests, please send it my way!)

## Testing

`make test` runs tests.

Note that the example tests use `Webtest`, which bypasses `app.yaml`. In particular, this means that these tests won't cover any `login:` behavior specified in `app.yaml`.

See the [Webtest Doc](http://webtest.pythonpaste.org/en/latest/api.html#module-webtest) for more on Webtest.

## Deploying

`gcloud init` will let you log in and specify a default app id (project). Thereafter, `make deploy` deploys to that app id.

By default, each deploy gets a new version. To control the version, add `--version` to the `gcloud` command in `Makefile`.  

## License

No license. This is unwarrantied, use-at-your-own-riskware. It's mostly pieced together from App Engine documentation and public sources, plus a tiny bit of my own code that you're welcome to.

