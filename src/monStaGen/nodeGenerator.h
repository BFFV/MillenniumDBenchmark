/*
 * nodeGenerator.h
 *
 *  Created on: Sep 26, 2016
 *      Author: wilcovanleeuwen
 */

#ifndef NODEGENERATOR_H_
#define NODEGENERATOR_H_

#include <random>
#include "../config.h"
#include "graphNode.h"

namespace std {

class nodeGenerator {
private:
	void addNode(config::edge & edgeType, int distrShift, bool findSourceNode);
	int getNumberOfICs(distribution distr, bool addSourceNode);
public:
	default_random_engine* randomGenerator;
	pair< vector<graphNode>, vector<graphNode> >* nodes;
	config::config* conf;
	int birthIdSubject;
	int birthIdObject;

	nodeGenerator();
	nodeGenerator(config::edge & edgeType, int birthIdSub, int birthIdOb, default_random_engine* randomGenerator, pair< vector<graphNode>, vector<graphNode> >* nodes, config::config* conf);
	virtual ~nodeGenerator();

	void addSubjectNodes(config::edge & edgeType, int distrShift, int graphNumber);
	void addObjectNodes(config::edge & edgeType, int distrShift, int graphNumber);

};

} /* namespace std */

#endif /* NODEGENERATOR_H_ */
