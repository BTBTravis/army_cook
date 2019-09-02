Army Cook Bot
======
**Army Cook Bot** is a twitter bot that tweets about WWII cooking, so far just recipes.

#### Twitter account: [@ArmyCookBot1](https://twitter.com/ArmyCookBot1)

#### Example Tweets:

> Got 7 gallons beef stock, 2 pounds rice, 5 pounds beef (shank, neck, etc.), and 1 bunch parsley sitting around the camp? How about Beef soup?

## Inspiration
* https://www.are.na/travis-shears/twitter-bots

## Sources
* https://archive.org/details/1942TM10-405

## License
* see [LICENSE](https://github.com/BTBTravis/army_cook/blob/master/LICENCE.md) file

## Version history
* [v0.0.6.alpha.1](https://github.com/BTBTravis/army_cook/releases/tag/v0.0.5)
  Up and running with master.txt and sayings.txt in config maps
* [v0.0.4](https://github.com/BTBTravis/army_cook/releases/tag/v0.0.3)

## Dev
**Run locally**

1. get the correct version of python running, `$ pipenv shell`
1. then install the app to local, `$ pip install --editable .`
1. then run app with, `$ ORIGIN_DATE="2019,8,30" DEV_ENV=1 armycook`
1. simply update code and rerun while in dev

**Update master.txt k8s config map:**
`$ kubectl create configmap master-txt --from-file ./master.txt --namespace armycook`

## Dev Links
* [Tweepy Docs](http://docs.tweepy.org/en/latest/api.html)
* [Docker python](https://docs.docker.com/samples/library/python/)

## Contact
#### Travis Shears
* Homepage: [personal site](https://travisshears.com)
* e-mail: t at travisshears.com
* Twitter: [@travisshears](https://twitter.com/travisshears)
