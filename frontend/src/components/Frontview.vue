<template>
<div id="app">

 <h3>Enter your Data</h3>
    <b-form @submit="submit">
      <b-form-group id="input-group-1" label="Name" label-for="input-1">
        <b-form-textarea
          id="input-1"
          type="text"
          v-model="dataentry.name"
          
          placeholder="Enter the Name"
          
        ></b-form-textarea>
      </b-form-group>

      <b-form-group id="input-group-2" label="Department" label-for="input-2">
        <b-form-textarea
          id="input-2"
          type="text"
          v-model="dataentry.about"
          placeholder="Type your Department here"
          rows=8
        ></b-form-textarea>
      </b-form-group>
    <b-button pill v-on:Click="submit" id="button-1" type="submit" variant="dark">Submit</b-button>
     
  </b-form>
    
  </div>

</template>
<script>
import axios from 'axios';
export default{
 
  data(){
    return {
       dataentry:{
        name:"",
        about:"",
      },
    };
  },
  methods:{
    submit:function(){
      const path = 'http://127.0.0.1:5000/dataentry'
      axios.post(path, {
        name:this.dataentry.name,
        about:this.dataentry.about,
        }
      )
      .then(response => {
        console.log(response);
      })
      .catch(err =>{
        console.log(err);
      });
    },
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Castoro&display=swap');
#app {
  font-family: 'Lato', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
#input-group-1 {
  margin-left:25%;
  margin-bottom: 20px;
  width: 50%;
  padding-left: 80px;
  margin-top: 50px;
  font-weight:bold;
 
}
h3{
  margin-left:40%;
  margin-top:20px;
  font-family: 'Castoro', serif;
}
#input-group-2{
  margin-left:25%;
  margin-bottom: 20px;
  width:50%;
  padding-left:80px;
 
  font-weight:bold;
}
#button-1{
margin-left:50%;
} 
.nav-bar{
  padding-left: 50px;;
}
.link{
  padding-right:100px;
  font-size: 20px;
  color:white;
}
</style>