import React from 'react'
import axios, { post } from 'axios';
import AuthService from "../services/auth.service";

const currentUser = AuthService.getCurrentUser();
console.log(currentUser)

class FileUpload extends React.Component {


  constructor(props) {
    super(props);
    this.state ={
      file:null,
      category:null,
      username:null
    }
    this.onFormSubmit = this.onFormSubmit.bind(this)
    this.onChange = this.onChange.bind(this)
    this.fileUpload = this.fileUpload.bind(this)
    this.onCategoryChange = this.onCategoryChange.bind(this);
  }

  onFormSubmit(e){
    e.preventDefault() // Stop form submit
    this.fileUpload(this.state.file).then((response)=>{
      console.log(response.data);
      alert("Upload Successful")
      this.setState({file:null})
      this.setState({category:null})
      e.target.reset();
    })
  }

  onChange(e) {
    this.setState({file:e.target.files[0]})
  }

  onCategoryChange(e){
        this.setState({ category: e.target.value });
        console.log(e.target.value)
  }

  fileUpload(file){
    const url = "http://10.0.0.129:5000/api/upload";
    //const url = 'http://example.com/file-upload';
    const formData = new FormData();
    formData.append('file',file)
    formData.append('category',this.state.category)
    formData. append('username', currentUser.username)
    console.log(this.state.username)
    console.log(this.state.category)
    console.log(...formData)
    const config = {
        headers: {
            'content-type': 'multipart/form-data'
        }
    }
    return  post(url, formData,config)
   
  }

//   const login = (username, password) => {
//     return axios
//       .post(API_URL + "signin", {
//         username,
//         password,
//       })
//       .then((response) => {
//         const users = response.data
//         console.log(response.data)
//         if (response.data.accessToken) {
//           localStorage.setItem("user", JSON.stringify(users));
//           console.log('users', users)
//         }
  
//         return response.data;
//       });
//   };

  render() {
    return (
      <form onSubmit={this.onFormSubmit}>
        <h1>File Upload</h1>
        <input type="file" onChange={this.onChange} />
        <button type="submit">Upload</button>

        <div>
              <select value={this.state.category} onChange={this.onCategoryChange}> 
                  <option name="Grocery"> Grocery</option>
                  <option name="Shopping">Shopping</option>
                  <option name="Rent"> Rent</option>
                  <option name="House Maintainence"> Maintainence</option>
              </select>
        </div>


        
      </form>
   )
  }
}



export default FileUpload

// import React, { Component } from "react";
// import UploadService from "../services/upload-file.service";

// export default class UploadFiles extends Component {
//   constructor(props) {
//     super(props);
//     this.selectFile = this.selectFile.bind(this);
//     this.upload = this.upload.bind(this);

//     this.state = {
//       selectedFiles: undefined,
//       currentFile: undefined,
//       progress: 0,
//       message: "",

//       fileInfos: [],
//     };
//   }

//   componentDidMount() {
//     UploadService.getFiles().then((response) => {
//       this.setState({
//         fileInfos: response.data,
//       });
//     });
//   }

//   selectFile(event) {
//     this.setState({
//       selectedFiles: event.target.files,
//     });
//   }

//   upload() {
//     let currentFile = this.state.selectedFiles[0];

//     this.setState({
//       progress: 0,
//       currentFile: currentFile,
//     });

//     UploadService.upload(currentFile, (event) => {
//       this.setState({
//         progress: Math.round((100 * event.loaded) / event.total),
//       });
//     })
//       .then((response) => {
//         this.setState({
//           message: response.data.message,
//         });
//         return UploadService.getFiles();
//       })
//       .then((files) => {
//         this.setState({
//           fileInfos: files.data,
//         });
//       })
//       .catch(() => {
//         this.setState({
//           progress: 0,
//           message: "Could not upload the file!",
//           currentFile: undefined,
//         });
//       });

//     this.setState({
//       selectedFiles: undefined,
//     });
//   }

//   render() {
//     const {
//       selectedFiles,
//       currentFile,
//       progress,
//       message,
//       fileInfos,
//     } = this.state;

//     return (
//       <div>
//         {currentFile && (
//           <div className="progress">
//             <div
//               className="progress-bar progress-bar-info progress-bar-striped"
//               role="progressbar"
//               aria-valuenow={progress}
//               aria-valuemin="0"
//               aria-valuemax="100"
//               style={{ width: progress + "%" }}
//             >
//               {progress}%
//             </div>
//           </div>
//         )}

//         <label className="btn btn-default">
//           <input type="file" onChange={this.selectFile} />
//         </label>

//         <button
//           className="btn btn-success"
//           disabled={!selectedFiles}
//           onClick={this.upload}
//         >
//           Upload
//         </button>

//         <div className="alert alert-light" role="alert">
//           {message}
//         </div>

//         <div className="card">
//           <div className="card-header">List of Files</div>
//           <ul className="list-group list-group-flush">
//             {fileInfos &&
//               fileInfos.map((file, index) => (
//                 <li className="list-group-item" key={index}>
//                   <a href={file.url}>{file.name}</a>
//                 </li>
//               ))}
//           </ul>
//         </div>
//       </div>
//     );
//   }
// }