from ontobio.ontol_factory import OntologyFactory

# Create ontology factory instance
ofactory = OntologyFactory()

# Load the MONDO ontology
ontology = ofactory.create('mondo')

# Get the term for Parkinson's disease
parkinsons_term = ontology.search('Parkinson disease')[0]

# Get the direct children IDs of Parkinson's disease
children_ids = ontology.children(parkinsons_term)

# Print labels and MONDO id's of the children terms
for child_id in children_ids:
  print(f"Name: {ontology.label(child_id)}, ID: {child_id}")
