import { useEffect, useState } from "react"
import './resumeform.styles.css'
import InputField from "../input-field/input-field.component"

const defaultField = {
    "id": '',
    "name": "",
    "email": "",
    "dob": "",
    "state": "",
    "gender": "",
    "preferred_locations": "",
}
const indianStates = [
  "Maharashtra",
  "Karnataka",
  "Tamil Nadu",
  "Uttar Pradesh",
  "Gujarat",
  "Rajasthan",
  "West Bengal",
  "Madhya Pradesh",
  "Kerala",
  "Bihar"
];
const GENDER = ["male","female","other"]
const indiaDataLocations = [
  "ap-south-1",   // Mumbai - AWS
  "me-south-1",   // Middle East (closest for some India use-cases)
  "IN-Mumbai",    // Azure India Central
  "IN-Pune",      // Azure India South
  "India West",   // GCP Mumbai
  "India South"   // GCP Delhi / Chennai (if available)
];


const ResumeForm = () => {

    const [formField, setFormField] = useState(defaultField);
    const [image, setImage] = useState(null);
    const [resumeFile, setResumeFile] = useState(null);
    const {id, name, email, dob, state, gender,preferred_locations, image_path, resume_file_path } = formField;

    const resetFormField = () => {
        setFormField(defaultField);
        setImage(null);
        setResumeFile(null);
    }

    const changeHandler = (e) => {
       let {name : inputName, value} = e.target 
       setFormField({...formField, [inputName] : value})
    }
    const checkBoxHandler = (e) => {
        const value = e.target.value;
        setFormField(prev => {
            const current = [...prev.preferred_locations]
            if(current.includes(value)){
                return { ...prev, preferred_locations : current.filter(loc => loc !== value) }
            }
            else{
                return { ...prev, preferred_locations : [...current, value]} ;
            }
        })
    }
    const submitHandler = async (e) => {
        e.preventDefault();
        const payload = new FormData();
        for (const key in formField) {
            if (key === 'id') continue;

            const value = formField[key];
            
            if(Array.isArray(value)){ // preferred_locations
                payload.append(key, value.join(','))
            }
            else{
                payload.append(key, formField[key])
            }
        }
            payload.append('image', image)
            payload.append('resume_file', resumeFile)
        
            const url = "http://127.0.0.1:8000/resumes/upload"
            try{
                const res = await fetch(url, {
                    'method' : 'post',
                    'body' : payload
                })
                const data = await res.json()
                if(!res.ok){
                    alert(data.detail || "Something went wrong");
                    return;
                }
                alert('Form submitted')
                console.log(data)
                resetFormField();
            }catch(e){
                console.log("Error in form submit: ",e)
            }
    }
    return(
        <div className="resume-form-container">
            <h2>Upload resume here</h2>
            <form onSubmit={submitHandler}>
                <InputField
                    label={"Name"}
                    id= "name"
                    required = {true}
                    type="text"
                    name="name"
                    value={name}
                    onChange={changeHandler}
                />
                <InputField
                    label={"Email"}
                    id= "email"
                    required = {true}
                    type="email"
                    name="email"
                    value={email}
                    onChange={changeHandler}
                />
                <InputField
                    label={"Date Of Birth"}
                    id= "dob"
                    required = {true}
                    type="date"
                    name="dob"
                    value={dob}
                    onChange={changeHandler}
                />
                <div className="form-input">
                    <label>State:</label>
                    <select name="state" value={state} onChange={changeHandler} required>
                        <option value="" disabled hidden>Select state</option>
                        {
                            indianStates.map(indianState => (
                                <option key={indianState} value={indianState}>{indianState}</option>
                            ))
                        }
                    </select>
                </div>
                <div className="form-input">
                    <label>Gender</label>
                    <div className="radio-group">
                        {   GENDER.map(gen => (
                            <label key={gen}>
                                
                                <input 
                                    type="radio"
                                    name="gender"
                                    value={gen}
                                    checked={gender === gen}
                                    onChange={changeHandler}
                                    required
                            />
                            {gen}
                            </label>
                        ))
                        }
                    </div>
                </div>
                <div className="form-input">
                    <label> Preferred locations:
                        {
                            indiaDataLocations.map(loc =>(
                                <label key={loc} > 
                                    <input
                                        // required = {true}
                                        type="checkbox"
                                        name="preferred_locations"
                                        value={loc}
                                        onChange={checkBoxHandler}
                                    />
                                    {loc}
                                </label>
                            ))
                        }
                    </label>
                </div>
                <InputField
                    label={"Upload image"}
                    id= "image"
                    required = {true}
                    type="file"
                    accept = 'image/*'
                    onChange = { e => setImage(e.target.files[0])}
                />
                <InputField
                    label={"Upload resume"}
                    id= "resume"
                    required = {true}
                    type="file"
                    accept = '.pdf, .doc, .docx'
                    onChange = { e => setResumeFile(e.target.files[0])}
                />
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}

export default ResumeForm