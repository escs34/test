

<?php
/* PHP JSON parser sample */
    $data_str = file_get_contents('gfriend.json');
    $json = json_decode($data_str, true);
?>
 
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>PHP JSON parser sample</title>
    </head>
   
    <body>
        <h2 id="gname"><?php
            echo $json['name'];
            if (array_key_exists('alias', $json) )
                printf(" (%s)", $json['alias']);
        ?></h2>
        <p>멤버 구성: <span id="members"><?php
            echo implode(', ', $json['members']); ?></span></p>
        <h3>앨범 목록</h3>
        <ul id="albums"><?php
            foreach ($json['albums'] as $key => $value) {
                printf("<li>%s: %s</li>\n", $key, $value);
            }
        ?></ul>
    </body>
</html>