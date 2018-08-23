#!/bin/bash

echo '# download composer.phar #'
curl -sS https://getcomposer.org/installer | php
#php -r "readfile('https://getcomposer.org/installer');" | php
 
echo '# composer require studio-42/elfinder 2.1.x@dev #'
php composer.phar require studio-42/elfinder 2.1.x@dev

echo '# make synlink css, img, js #'
ln -s ./vendor/studio-42/elfinder/css
ln -s ./vendor/studio-42/elfinder/img
ln -s ./vendor/studio-42/elfinder/js
ln -s ./vendor/studio-42/elfinder/sounds

echo '# mkdir files #'allow
mkdir files

echo '# mkdir .tmp #
mkdir .tmp

echo '# make .tmp/.htaccess #'
cat << \EOD > .tmp/.htaccess
order deny,allow
deny from all
EOD

echo '# make connector.php #'
cat << \EOD > connector.php
 array(
		array(
			'driver'        => 'LocalFileSystem',           // driver for accessing file system (REQUIRED)
			'path'          => ELFINDER_ROOT_PATH . '/files/', // path to files (REQUIRED)
			'URL'           => ELFINDER_ROOT_URL  . '/files/', // URL to files (REQUIRED)
			'uploadDeny'    => array('all'),                // All Mimetypes not allowed to upload
			'uploadAllow'   => array('image', 'text/plain'),// Mimetype `image` and `text/plain` allowed to upload
			'uploadOrder'   => array('deny', 'allow'),      // allowed Mimetype `image` and `text/plain` only
			'accessControl' => 'access'                     // disable and hide dot starting files (OPTIONAL)
		)
	),
	'optionsNetVolumes' => array(
		'*' => array(
			'tmbURL'    => ELFINDER_ROOT_URL  . '/files/.tmb',
			'tmbPath'   => ELFINDER_ROOT_PATH . '/files/.tmb',
			'syncMinMs' => 30000
		)
	)
);

//////////////////////////////////////////////////////////////////////
// load composer autoload.php
require './vendor/autoload.php';

// Enable FTP connector netmount
if ($useFtpNetMount) {
	elFinder::$netDrivers['ftp'] = 'FTP';
}

/**
 * Simple function to demonstrate how to control file access using "accessControl" callback.
 * This method will disable accessing files/folders starting from '.' (dot)
 *
 * @param  string  $attr  attribute name (read|write|locked|hidden)
 * @param  string  $path  file path relative to volume root directory started with directory separator
 * @return bool|null
 **/
function access($attr, $path, $data, $volume) {
	return strpos(basename($path), '.') === 0       // if file/folder begins with '.' (dot)
		? !($attr == 'read' || $attr == 'write')    // set read+write to false, other (locked+hidden) set to true
		:  null;                                    // else elFinder decide it itself
}

// run elFinder
$connector = new elFinderConnector(new elFinder($opts));
$connector->run();

// end connector
EOD

echo '# make index.html #'
cat << \EOD > index.html


	
		
		elFinder 2.1.x source version with PHP connector
		

		
		

	
	

		
		

	

EOD

echo '# make main.js #'
cat << \EOD > main.js
"use strict";
/**
 * elFinder client options and main script for RequireJS
 *
 **/
(function(){
	var // jQuery and jQueryUI version
		jqver = '3.2.1',
		uiver = '1.12.1',
		
		// Detect language (optional)
		lang = (function() {
			var locq = window.location.search,
				fullLang, locm, lang;
			if (locq && (locm = locq.match(/lang=([a-zA-Z_-]+)/))) {
				// detection by url query (?lang=xx)
				fullLang = locm[1];
			} else {
				// detection by browser language
				fullLang = (navigator.browserLanguage || navigator.language || navigator.userLanguage);
			}
			lang = fullLang.substr(0,2);
			if (lang === 'ja') lang = 'jp';
			else if (lang === 'pt') lang = 'pt_BR';
			else if (lang === 'ug') lang = 'ug_CN';
			else if (lang === 'zh') lang = (fullLang.substr(0,5).toLowerCase() === 'zh-tw')? 'zh_TW' : 'zh_CN';
			return lang;
		})(),
		
		// elFinder options (REQUIRED)
		// Documentation for client options:
		// https://github.com/Studio-42/elFinder/wiki/Client-configuration-options
		opts = {
			width: '100%',
			height: '100%',
			resizable: false,
			url : 'connector.php', // connector URL (REQUIRED)
			lang: lang             // auto detected language (optional)
		},
		
		// Start elFinder (REQUIRED)
		start = function(elFinder) {
			// load jQueryUI CSS
			elFinder.prototype.loadCss('//cdnjs.cloudflare.com/ajax/libs/jqueryui/'+uiver+'/themes/smoothness/jquery-ui.css');
			
			$(function() {
				// Optional for Japanese decoder "extras/encoding-japanese.min"
				if (window.Encoding && Encoding.convert) {
					elFinder.prototype._options.rawStringDecoder = function(s) {
						return Encoding.convert(s,{to:'UNICODE',type:'string'});
					};
				}
				// Make elFinder (REQUIRED)
				$('#elfinder').elfinder(opts);
			});
		},
		
		// JavaScript loader (REQUIRED)
		load = function() {
			require(
				[
					'elfinder'
					, (lang !== 'en')? 'elfinder.lang' : null    // load detected language
				//	, 'extras/quicklook.googledocs'              // optional preview for GoogleApps contents on the GoogleDrive volume
				//	, (lang === 'jp')? 'extras/encoding-japanese.min' : null // optional Japanese decoder for archive preview
				],
				start,
				function(error) {
					alert(error.message);
				}
			);
		},
		
		// is IE8? for determine the jQuery version to use (optional)
		ie8 = (typeof window.addEventListener === 'undefined' && typeof document.getElementsByClassName === 'undefined');

	// config of RequireJS (REQUIRED)
	require.config({
		baseUrl : 'js',
		paths : {
			'jquery'   : '//cdnjs.cloudflare.com/ajax/libs/jquery/'+(ie8? '1.12.4' : jqver)+'/jquery.min',
			'jquery-ui': '//cdnjs.cloudflare.com/ajax/libs/jqueryui/'+uiver+'/jquery-ui.min',
			'elfinder' : 'elfinder.min',
			'elfinder.lang': [
				'i18n/elfinder.'+lang,
				'i18n/elfinder.fallback'
			]
		},
		waitSeconds : 10 // optional
	});

	// load JavaScripts (REQUIRED)
	load();

})();
asdfasdd's都是sh'd'f

echo '# make vendor/.htaccess #'
cat << \EOD > vendor/.htaccess
order deny,allow
deny from all
EOD

#echo "# rm $0 #"
#rm $0

echo '# Finish!! #'
