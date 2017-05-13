# websitetopdf

Simple app to demonstrate the usage of
[heroku-buildpack-wkhtmltopdf](https://github.com/simplefractal/heroku-buildpack-wkhtmltopdf).


## Sample

You can see this app running on
[websitetopdf.herokuapp.com](https://websitetopdf.herokuapp.com/).

## Deploying

```bash
git clone https://github.com/turicas/websitetopdf.git
cd websitetopdf

heroku create

heroku buildpacks:add https://github.com/simplefractal/heroku-buildpack-wkhtmltopdf.git
heroku buildpacks:add heroku/python

git push heroku master
```

> Note: `heroku/python` is only needed by this app for demonstration purposes.
> You just need to add the `simplefractal/heroku-buildpack-wkhtmltopdf` buildpack to
> your app and then execute `/app/bin/wkhtmltopdf` whenever you need.
