<template>
  <div>
  <div id="drag-drop">
  
    
  </div>
</div>
</template>

<script setup>
import Uppy from '@uppy/core';
import DragDrop from '@uppy/drag-drop';
import Dashboard from '@uppy/dashboard'
import '@uppy/dashboard/dist/style.css'
import Webcam from '@uppy/webcam'
import XHRUpload from '@uppy/xhr-upload'
import '@uppy/webcam/dist/style.css'
import '@uppy/core/dist/style.min.css';
import '@uppy/drag-drop/dist/style.min.css';

// onMounted(() => {
//   console.debug('test');
//   new Uppy()
//   .use(DragDrop, { target: '#drag-drop' })
//   .use(XHRUpload, {
//   endpoint: 'http://localhost:8000/upload',
// })
//   .use(Webcam)
// }) 
const uppy = new Uppy({
  debug: true,
  autoProceed: false,
})

onMounted(() => {
uppy.use(Webcam)
uppy.use(Dashboard, {
  inline: true,
  target: 'body',
  plugins: ['Webcam'],
})
.use(DragDrop, { target: '#drag-drop' })
.use(XHRUpload, {
  bundle: true,
  endpoint: 'http://localhost:8000/upload',
  allowedMetaFields: ['something'],
  fieldName: 'files',
})
}) 

</script>


