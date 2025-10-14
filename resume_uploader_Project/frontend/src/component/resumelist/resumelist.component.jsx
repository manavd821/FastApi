import { useEffect, useState } from "react"
import './resumelist.styles.css'
const  ResumeList = () => {
    const [resumes, setResumes] = useState([]);

  useEffect(() => {
    const fetchResume = async () => {
      const url = "http://127.0.0.1:8000/resumes/get";
      try {
        const res = await fetch(url);
        const data = await res.json();
        console.log(data)   // ✅ parse JSON
        setResumes(data);   // ✅ store JSON array
      } catch (e) {
        console.log("Error:", e);
      }
    };

    fetchResume();
  }, []);
     return (
      
            <div className="resume-list-container">
              { (!resumes.length) ? (<div>No resumes are there.</div>) : (
                <table className="table-container">
                  <thead>
                    <tr>
                      <th>ID</th>
                      <th>NAME</th>
                      <th>EMAIL</th>
                      <th>DOB</th>
                      <th>STATE</th>
                      <th>GENDER</th>
                      <th>PREFERED LOCATION</th>
                      <th>IMAGE</th>
                      <th>RESUME</th>
                    </tr>
                  </thead>
                  <tbody>
                    {
                      resumes.map(resume => (
                        <tr key = {resume.id} >
                          <td>{resume.id}</td>
                          <td>{resume.name}</td>
                          <td>{resume.email}</td>
                          <td>{resume.dob}</td>
                          <td>{resume.state}</td>
                          <td>{resume.gender}</td>
                          <td>{resume.preferred_locations}</td>
                          <td>
                            <a href={resume.image_path} target="_blank" rel="noreferrer">
                              <img
                                alt="resume"
                                src={resume.image_path}
                                width={150}
                                style={{ borderRadius: "6px", cursor: "pointer" }}
                              />
                          </a>
                          </td>
                          <td>
                            <a href={resume.resume_file_path} target="_blank">Download</a>
                          </td>
                        </tr>
                      ))
                    }
                  </tbody>
                </table>
              ) }
            </div>
        )  
}
export default ResumeList