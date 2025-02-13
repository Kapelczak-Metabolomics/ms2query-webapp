# Adjusted Streamlit-based code for MS2Query Web App using MS2Library
import streamlit as st
import os
from ms2query.ms2library import MS2Library

# Create upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
	os.makedirs(UPLOAD_FOLDER)

# Streamlit app title
st.title("MS2Query Web App")

# File upload widgets
ms2_file = st.file_uploader("Upload MS2 File", type=["ms2"])
library_file = st.file_uploader("Upload Custom Library File", type=["sqlite"])

# Process button
if st.button("Process"):
	if ms2_file and library_file:
		# Save uploaded files
		ms2_file_path = os.path.join(UPLOAD_FOLDER, ms2_file.name)
		library_file_path = os.path.join(UPLOAD_FOLDER, library_file.name)

		with open(ms2_file_path, "wb") as f:
			f.write(ms2_file.read())

		with open(library_file_path, "wb") as f:
			f.write(library_file.read())

		# Process files using MS2Library
		output_file_path = os.path.join(UPLOAD_FOLDER, 'output.csv')

		try:
			# Load the library
			ms2_library = MS2Library(
				sqlite_file_name=library_file_path,
				s2v_model_file_name="spec2vec_model_file",
				ms2ds_model_file_name="ms2ds_model_file",
				s2v_embeddings_file_name="s2v_embeddings_file",
				ms2ds_embeddings_file_name="ms2ds_embeddings_file",
				ms2query_model_file_name=None
			)

			# Placeholder for processing logic (adjust as needed)
			# ms2_library.query(ms2_file_path, output_file_path)

			st.success("Processing Complete! Download the output file below.")

			# Provide download link
			with open(output_file_path, "rb") as f:
				st.download_button(
					label="Download Output File",
					data=f,
					file_name="output.csv",
					mime="text/csv"
				)
		except Exception as e:
			st.error(f"Error processing files: {str(e)}")
	else:
		st.warning("Please upload both an MS2 file and a library file.")