import React from 'react';
import { StyleSheet, Text, View, Button, Image } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import Constants from 'expo-constants';
import * as Permissions from 'expo-permissions';

import 'here-js-api/scripts/mapsjs-core';
import 'here-js-api/scripts/mapsjs-service';

import EXIF from 'exif-js';

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});


// export default function App() {
//   return (
//     <View style={styles.container}>
//       <Text>Hello World!</Text>
//       <Button
//         onPress={onPressUpload}
//         title="Take Photo of Landmark"
//         color="#841584"
//         accessibilityLabel="Upload image"
//       />
//     </View>
//   );
// }

const onPressUpload = () => {

  console.log('pressed');

  ImagePicker.launchCameraAsync({})

}

export default class ImagePickerExample extends React.Component {
  state = {
    image: null,
  };

  render() {
    let { image } = this.state;

    return (
      <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
        <Button
          title="Take a photo of a landmark"
          onPress={this._pickImage}
        />
        {image &&
          <Image source={{ uri: image }} style={{ width: 200, height: 200 }} />}
      </View>
    );
  }

  componentDidMount() {
    this.getPermissionAsync();
  }

  getPermissionAsync = async () => {
    if (Constants.platform.ios) {
      const { status } = await Permissions.askAsync(Permissions.CAMERA, Permissions.CAMERA_ROLL);
      if (status !== 'granted') {
        alert('Sorry, we need camera roll permissions to make this work!');
      }
    }
  }

  _pickImage = async () => {
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.All,
      allowsEditing: true,
      aspect: [4, 4],
        exif: true
    });

    console.log(result);

    if (!result.cancelled) {
      this.setState({ image: result.uri });
    }

    // ImagePicker saves the taken photo to disk and returns a local URI to it
      let localUri = result.uri;
      let filename = localUri.split('/').pop();

      // Infer the type of the image
      let match = /\.(\w+)$/.exec(filename);
      let type = match ? `image/${match[1]}` : `image`;

      // Upload the image using the fetch and FormData APIs
      let formData = new FormData();
      // Assume "photo" is the name of the form field the server expects
      formData.append('photo', { uri: localUri, name: filename, type });

      if ('exif' in result) {
          if ('GPSLatitude' in result.exif) {
            formData.append('lat', result.exif.GPSLatitude);
            formData.append('lat_ref', result.exif.GPSLatitudeRef);
            formData.append('lon', result.exif.GPSLongitude);
            formData.append('lon_ref', result.exif.GPSLongitudeRef);
          }
      }

      return await fetch('http://arabia.herokuapp.com/upload', {
        method: 'POST',
        body: formData,
        header: {
          'content-type': 'multipart/form-data',
        },
      });

  };
}