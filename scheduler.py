import random

SIZE = 3;
ITER = 10000;

def gen_init_pop( c, p, d, t):
	chromosomes = [];

	for i in range (0, SIZE):
		chrom = [];
		for j in range(0, c):			
			gene = [];
			gene.append(random.randint(1, p)); #Prof
			gene.append(random.randint(1, t)); #time slot
			gene.append(random.randint(1, d)); #day
			chrom.append(tuple(gene));
		chromosomes.append(chrom);

	return chromosomes;

def fitness(chrom):

def cross_over(pop):

def mutation(pop):

def get_fittest(pop):


def main():

	line = raw_input();
	line = line.split(' ');
	d = int(line[0]);  #days
	t = int(line[1]);  #time slots

	c = int(raw_input()); #courses

	C = raw_input();
	C = C.split(' ');
	for i in range(0, c):
		C[i] = int(C[i]);

	p = int(raw_input()); #professors

	Profs = [];
	for i in range(0, p):
		courses = raw_input().split(' ');
		for j in range(0, len(courses)):
			courses[j] = int(courses[j]);

		Profs.append(courses[1:]);

	Sadness = [];
	for i in range(0, c):
		row = raw_input().split(' ');
		for j in range(0, len(row)):
			row[j] = int(row[j]);

		Sadness.append(row);

	pop = gen_init_pop(c, p, d, t); #population is made

	for i in range(0, ITER):

		print("iter " + i + ":    fitness: " + fitness(get_fittest(pop)) );
		pop = cross_over(pop);
		pop = mutation(pop);



main();	
