while (i < str.length) {
      if (j === 1) {
        outcast = str[i];
      } else if (j === 2 && (j + 1 !== undefined)) {
        outcast = `${str[i]}${str[i + 1]}`;
      }
      console.log(outcast);
      if (outcast !== '') {
        let newStr = str.replace(outcast, '');
        const reversed = newStr.split('').reverse().join('');
        if (newStr === reversed) {
          console.log(true);
          resultOutcast = outcast;
        }
      }
      
      i++;
      outcast = '';
    }