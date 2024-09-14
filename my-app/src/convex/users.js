import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const updateUser = mutation({
    args : {},
    handler : async (ctx, args) => {
        const identity = await ctx.auth.getUserIdentity();
        if (!identity){
            throw Error("No identity found!");
        }

        const user_document = await ctx.db
            .query("users")
            .filter(q => q.eq(q.field("subject"), identity.subject))
            .unique();
        
        if (user_document){
            await ctx.db.patch(user_document._id, identity);
        }else{
            await ctx.db.insert("users", identity);
        }
    }
})