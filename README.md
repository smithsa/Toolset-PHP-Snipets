# Toolset PHP Snippets

Toolset PHP Snippets python script that works to get php code customizable field snippets for [Wordpress Toolset Plugin](https://toolset.com/documentation/) custom fields.Included in the repository are (1) an executable script and (2) python script.

<img src="https://user-images.githubusercontent.com/1827606/46117042-a1606500-c1c4-11e8-81f2-a62fc88e05c6.png" alt="toolset snippet php screenshot" width="70%"/>


## Motivation
Adding custom fields to your template files are a tedious task which require a lot of lookup to find the custom fields variable names. This script automatically searches your database for the custom fields and displays them to you on a web page where you can easily copy custom field php output statments and paste them into your template.

## Prerequisites
*	[Python](https://www.python.org)
*	[MySQLdb](http://mysql-python.sourceforge.net/MySQLdb.html)
* 	[Chrome](https://www.google.com/chrome)

## Installation

1. Clone the repository.

    ```
    git clone git@github.com:smithsa/toolset-php-snipets.git
    ```

## Usage

### Running the script

**Command Line**
1. Navigate to the directory holding the contents of the repository

    ```
    cd toolset-php-snipets
    ```

2. run the *toolset-php-snipets.py* script. You will see a window appear in the top left corner.

    ```
    python toolset-php-snipets.py
    ```


**Executable**
1. Navigate to the directory holding the contents of the repository

2. Click on the file *toolset-php-snippets.command* and the script will run. You will see a window appear in the top left corner.

### Using the script

Once the script is up and running, you can use the following directions to use the script.

1. Enter the databse name in the window

    ![toolset snippet php window screenshot](https://user-images.githubusercontent.com/1827606/46117041-a1606500-c1c4-11e8-88eb-f4c4d910fc8e.png)

2. Once step 1 is complete, a new tab will be opened in your Chrome browser showing a page titled *Toolset PHP Snippets: [your datbase name]*. You can use this page to copy snippets as you like. You can get (1) an echo statement of the custom field inside PHP template tags, (2) the custom field as a variable, (3) the custom field as a variable inside PHP template tags.

    ![toolset snippet php usage](https://user-images.githubusercontent.com/1827606/46117043-a1606500-c1c4-11e8-961e-b5891c703bd0.gif)


## Built With
*	[Python](https://www.python.org)
*	[Clipboard.js](https://clipboardjs.com)

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

MIT © [Sade Smith](https://sadesmith.com)
