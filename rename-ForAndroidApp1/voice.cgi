#!/usr/bin/perl

$DIR = "voice";
opendir(DIR, $DIR);
@filelist = readdir(DIR);
closedir(DIR);

foreach $file (@filelist) {
	if ($file eq "." || $file eq "..") { next; }
	opendir(DIR, "$DIR/$file");
	@sublist = readdir(DIR);
	closedir(DIR);

	foreach $file2 (@sublist) {
		if ($file2 eq "." || $file2 eq "..") { next; }
		opendir(DIR, "$DIR/$file/$file2");
		@subsublist = readdir(DIR);

		foreach $file3 (@subsublist) {
			$fname = "$DIR/$file/$file2/$file3";
			$fname2 = "$DIR/$file/$file2/$file$file3";
			`mv $fname $fname2`;
		}
		$fname = "$DIR/$file/$file2/*";
		$fname2 = "$DIR/";
		`mv $fname $fname2`;
	}
}
