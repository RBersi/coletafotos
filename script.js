document.addEventListener('DOMContentLoaded', function () {
  const uppy = new Uppy.Core()
    .use(Uppy.Dashboard, {
      inline: true,
      target: '#drag-drop-area',
      note: 'Arraste suas fotos aqui ou clique para selecionar',
      proudlyDisplayPoweredByUppy: false
    })
    .use(Uppy.Tus, { endpoint: 'https://tusd.tusdemo.net/files/' });

  uppy.on('complete', (result) => {
    alert('Fotos enviadas com sucesso!');
    console.log('Uploads completos:', result.successful);
  });
});
