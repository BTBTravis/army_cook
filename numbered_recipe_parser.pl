#!/usr/bin/perl
use strict;
use warnings;


#my $filename = 'data.txt';
my @recipes;
my $i = 0;

while (<>) {
    my $txt = $_;
    my $title = $_;
    if (/^\d+\. [A-Z]/) {
        if (@recipes > 0) {
	    my $existingdir = './recipes';
	    my $fname = $recipes[0];
	    $fname =~ s/\n//g;
	    mkdir $existingdir unless -d $existingdir; # Check if dir exists. If not create it.
	    open my $fileHandle, ">>", "$existingdir/$i-a.txt" or die "Can't open '$existingdir/$fname.txt'\n";
	    foreach (@recipes) {
		print $fileHandle $_;
	    }
	    close $fileHandle;
            @recipes = ();
            $i++;
        }

        chomp $txt;
        chomp $title;
        $title =~ s/^[^A-Z]+//g; # trim front off number and spaces
        $title =~ s/[^a-z|A-Z|\s]//g;
        $title =~ s/\s/_/g;
        #print $txt . "\n";
        #print $title . "\n";
        #push @recipes, ($title . "|" . $txt . "\n");
        push @recipes, ($title ."\n");
    } else {
	push @recipes, $txt;
    }
}




        #push @done_tasks, $_;
        #$last_task_type = $done_type;
    #} elsif (/^\s{$indent}- \[/) {
    #while (my $row = <$fh>) {
      #chomp $row;
      #print "$row\n";
    #}
#my @done_tasks;
#my @todo_tasks;
#my $todo_type = "todo";
#my $done_type = "done";
#my $last_task_type = "none";
#my $has_cacled_indent = 0;
#my $indent = 0;

#while (<>) {
    #if (not $has_cacled_indent) {
        #$indent = $_ =~ s/^(\s+).+/$1/rg;
        #$indent = length($indent);
        #$indent--;
        #$has_cacled_indent = 1;
    #}

    #if (/^\s{$indent}- \[X/) {
        #push @done_tasks, $_;
        #$last_task_type = $done_type;
    #} elsif (/^\s{$indent}- \[/) {
        #push @todo_tasks, $_;
        #$last_task_type = $todo_type;
    #} elsif ($last_task_type eq $todo_type && @todo_tasks > 0) {
        #$todo_tasks[@todo_tasks - 1] = $todo_tasks[@todo_tasks - 1] . $_;
    #} elsif ($last_task_type eq $done_type && @done_tasks > 0) {
        #$done_tasks[@done_tasks - 1] = $done_tasks[@done_tasks - 1] . $_;
    #}
#}

#foreach (@todo_tasks) {
    #print;
#}

#foreach (@done_tasks) {
    #print;
#}
