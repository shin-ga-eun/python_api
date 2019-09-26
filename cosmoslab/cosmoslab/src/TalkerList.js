import React, { Component } from 'react'
import TalkerForm from './TalkerForm';
import TalkerItem from './TalkerItem';

class TalkerList extends Component {
    state = {
        maxNo: 1,
        boards: [
            {
                brdno: '예시',
                talker:'코스모스',
                text: '코스모스는 가을에 피어요.',
                analysisType:'morpAPI',
            },
         
        ],
         selectedBoard:{}
    }
    
    handleSaveData = (data) => {
        if (!data.brdno) {            // new : Insert
            this.setState({
                maxNo: this.state.maxNo+1,
                boards: this.state.boards.concat({brdno: this.state.maxNo, ...data }),
                selectedBoard: {},
                
            });
            console.log("넘버maxno:"+this.state.maxNo);
            console.log("insert값으로 들어왔음");

        } else {                                                        // Update
            this.setState({
                boards: this.state.boards.map(row => data.brdno === row.brdno ? {...data }: row),
                selectedBoard: {}
            })  

            console.log("넘버brdno:"+ data.brdno);
            console.log("update값으로 들어왔음");
  
        }
    }
    

    handleSelectRow = (row) => {
        this.setState({selectedBoard: row});
    }
    

    render() {
        const { boards, selectedBoard } = this.state;

        return (
            <div>
                <TalkerForm selectedBoard={selectedBoard} onSaveData={this.handleSaveData}/>

                
                    {
                        boards.map(row =>
                            (<TalkerItem key={row.brdno} row={row} onSelectRow={this.handleSelectRow} />)
                        )
                    }
             
            </div>
        );
    }
}
export default TalkerList;
