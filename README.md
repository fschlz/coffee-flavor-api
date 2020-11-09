# Coffee Flavor API

This is a simple JSON API that only runs locallyon your machine and provides the coffee flavors that have been defined by the Specialty Coffee Association (SCA) in their ["The Coffee Taster's Flavor Wheel"](https://sca.coffee/research/coffee-tasters-flavor-wheel).

# Usage

- You can run the API locally on your machine with Flask:

```shell
python -m coffee_flavor_api
```

- Flask will use port 5000 by default and display an inital JSON file

```
# Flask will server under this URL
# alternatively: use http://127.0.0.1:5000/
localhost:5000
```

- Try typing the following URLs into your browser

```
# all flavors
localhost:5000/flavors

# flavors associated with the overall category of fruity flavors
localhost:5000/flavors/fruity

# list of nuanced flavors associated with the category of berry-like flavors
localhost:5000/flavors/fruity/berry
```

## Disclaimer

I am in no way associated with the SCA and all credit for the Flavor Wheel goes to them.

The flavor wheel is published as a PDF file and I have translated it into a JSON file, as you can see in the ``/resources`` folder.

## License & Copyright

"The Coffee Taster's Flavor Wheel" by the SCA and WCR (©2016-2020) is distributed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

The same license applies here.

If you intend to use the Flavor Wheel in any way, please be mindful of the License.
