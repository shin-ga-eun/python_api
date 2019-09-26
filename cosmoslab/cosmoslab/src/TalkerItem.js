import React, { Component } from 'react'
import TextField from '@material-ui/core/TextField';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core/styles';
import { typography } from '@material-ui/system';
import TalkerChips from './TalkerChips';

const useStyles = makeStyles(theme => ({
  root: {
    padding: theme.spacing(3, 2),
    margin: theme.spacing(1),
  },
  button: {
    margin: theme.spacing(1),
  },
  textField: {
    marginLeft: theme.spacing(1),
    marginRight: theme.spacing(1),
  },

}));

class TalkerItem extends Component {
     
  //게시판 글 선택
  handleSelectRow = () => {
      const { row, onSelectRow } = this.props;
      onSelectRow(row);
  }    

  render() {
    const classes = useStyles.bind();

      return(
          <div>
            {/* 발화자 발화내용 start */}
             <Paper className = {classes.root}>

                <Grid container spacing = {1} item sm={12} >  
                   
                  
                    
                    <Grid item sm = {1} 
                      direction="column"
                      justify="flex-start"
                      alignItems="flex-start">
                      <Typography style={{ marginTop: 25, marginLeft: 20 }} >{this.props.row.brdno}</Typography>
                      <Typography variant="h5" style={{ marginTop: 25, marginLeft: 20, }} >{this.props.row.analysisType}</Typography>
                    </Grid>
                      
                    <Grid item sm = {2} direction="row" justify="flex-start" alignItems="flex-start" container>
                        <TextField
                            id="standard-read-only-input"
                            label="발화인"
                            value={this.props.row.talker}
                            className={classes.textField}
                            style={{ margin: 8 ,}}
                            margin="normal"
                            variant="filled"
                            InputProps={{
                                readOnly: true,
                                }}
                            // onClick={this.handleSelectRow}

                            />
                      </Grid> 
                  
                  <Grid item sm ={9} >
                    <Grid
                      container
                      direction="column"
                      justify="flex-start"
                      alignItems="stretch"
                    >

                      <TextField
                        id="outlined-full-width"
                        label="발화내용"
                        value={this.props.row.text}
                        className={classes.textField}
                        style={{ margin: 8 }}
                        fullWidth
                        margin="normal"
                        variant="filled"
                        InputProps={{
                            readOnly: true,
                            }}
                        onClick={this.handleSelectRow}

                       /> 
                      </Grid>

                      
                      {/* 분석 태그 start */}
                      <Grid
                        container
                        direction="column"
                        justify="flex-start"
                        alignItems="stretch"
                        >  
                      <TalkerChips/>
                      </Grid>

                      {/* 분석태그 end */}
                      </Grid>
                    
                </Grid>
              </Paper>
            {/* 발화자 발화내용 end */}
            
             </div>

      );
  }
}

export default TalkerItem;