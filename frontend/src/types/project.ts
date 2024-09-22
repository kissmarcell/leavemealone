import { Provider } from "@/constants/Values"

export type ProjectListRequest = ProjectType[]

export type IssueType = {
    id: number,
    name: string,
    state: string,
    url: string,
}

export type ProjectType = {
    issues: IssueType[],
    name: string,
    provider: Provider,
}