<template>
<div id="app">
  <b-navbar toggleable type="dark" variant="dark">
    <b-navbar-brand class="nav-bar">Featurepreneur</b-navbar-brand>
    <b-navbar-nav class=ml-auto>
        <b-nav-item class="link" href="/data">View Data</b-nav-item>
    </b-navbar-nav>
  </b-navbar>

  <div >
    <h3> LinkedIn Data Collection</h3>
    <b-form @submit="submit">
      <b-form-group id="input-group-1" label="Name" label-for="input-1">
        <b-form-textarea
          id="input-1"
          type="text"
          v-model="dataentry.name"
          
          placeholder="Enter the Name"
          
        ></b-form-textarea>
      </b-form-group>

      <b-form-group id="input-group-2" label="About" label-for="input-2">
        <b-form-textarea
          id="input-2"
          type="text"
          v-model="dataentry.about"
          placeholder="Type About"
          rows=8
        ></b-form-textarea>
      </b-form-group>
    <b-button pill v-on:Click="submit" id="button-1" type="submit" variant="dark">Submit</b-button>
     
  </b-form>
    
  </div>
</div>
</template>

<script>

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