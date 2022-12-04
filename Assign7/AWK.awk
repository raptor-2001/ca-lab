BEGIN {
	total=0;
	i = 1;
	max = -99999;
}
{
	totalSum = ($3+$4+$5) + ($6+$7+$8) + ($9+$10+$11) + ($12+$13+$14) + ($15+$16+$17);
	totalSum = totalSum/5;
	marks[i] = totalSum;
	name[i] = $2;
	i = i+1;
        max = (max > totalSum) ? max : totalSum;
}
END {
        for (i = 1; i < 10; ++i) {
      		if(marks[i]==max){
      			print name[i] "  " marks[i] "  "100;
      		}
      		else{
      			print name[i] "  " marks[i] "  " (marks[i]*100)/max;
      		}
        } 
}
