<?php
/**
 * Plugin Name: Shortcode Example
 * Description: A basic example of how a shortcode works in Wordpress. Lets the tag [shortcode-example] output a "This is an example of a shortcode."-statement.
 * Version: 1.0
 * Author: Kolguyev
 * Author URI: http://www.kolguyev.se
 * License: GPL
 */

defined('ABSPATH') or die("Direct access to this file has been denied.");

// The content the shortcode should return, i.e. what [shortcode-example] should represent
function shortcode_example_function() {
    $content = '';
    $content .= '<b> --- This is an example of a shortcode --- </b>';
    return $content;
}

// Let Wordpress tell about the new shortcode, called upon by [shortcode-example]
function register_example_shortcode(){
   add_shortcode('shortcode-example', 'shortcode_example_function');
}

add_action('init', 'register_example_shortcode');

?>
