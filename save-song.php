<?php
 $input = $_POST["songTextInput"];
 file_put_contents('savedsongs.js',$input . "\n", FILE_APPEND);
?>