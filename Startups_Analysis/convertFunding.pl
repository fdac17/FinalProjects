while($line = <>){
	if($line =~ /(\d*),(\d*),(\d*)/){
		print $1.$2.$3."\n"
	}
}
