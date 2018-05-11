use warnings;

open (FH1,"<","dict.txt");

while ($x = <FH1>){
	#if ($x =~ m/^p[^r].{2,15}/i){
	#if ($x =~ m/b$/){
	if ($x =~ m/^di/){
		push @x,$x;
	}
}
close FH1;

open (OUT, ">", "output.txt");
foreach (@x){
	print OUT $_;
}
close OUT;