import { useState } from "react";
import api from "../services/api";

export default function UploadResume() {

  const [file, setFile] = useState(null);

  const uploadResume = async () => {

    const formData = new FormData();

    formData.append("file", file);

    try {

      await api.post(
        "resume/upload/",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      alert("Resume Uploaded!");

    } catch (error) {

      console.log(error);

      alert("Upload Failed");

    }

  };

  return (
    <div>

      <h1>Upload Resume</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br />
      <br />

      <button onClick={uploadResume}>
        Upload Resume
      </button>

    </div>
  );
}