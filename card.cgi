#!/usr/bin/perl

$DIR = "card";
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
		$filename1 = "$DIR/$file/$file2/.1.png.dat";
		$filename1_after = "$DIR/$file-$file2-1.png.dat";
		$filename2 = "$DIR/$file/$file2/.camera.png.dat";
		$filename2_after = "$DIR/$file-$file2-camera.png.dat";
		`cp $filename1 $filename1_after`;
		`cp $filename2 $filename2_after`;
	}
}
