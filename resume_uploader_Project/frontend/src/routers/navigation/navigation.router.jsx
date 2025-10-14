import { Routes, Route } from 'react-router'
import ResumeForm from '../../component/resumeform/resumeform.component'
import ResumeList from '../../component/resumelist/resumelist.component'
import NavigationLayout from '../../component/navigation/navigation.comonent'

const Navigation = () => {
    return (
        <Routes>
            <Route path='/' element={<NavigationLayout/>}>
                <Route index element={<ResumeList/>} />
                <Route path='/form' element={<ResumeForm/>} />
            </Route>
        </Routes>
    )
}
export default Navigation;